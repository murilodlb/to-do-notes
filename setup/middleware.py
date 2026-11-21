import hashlib
import json

from django.core.cache import cache
from django.http import HttpResponseRedirect


class DuplicatePostProtectionMiddleware:
    """Block rapid identical POST submissions from the same user/session."""

    LOCK_TIMEOUT_SECONDS = 3

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method != "POST":
            return self.get_response(request)

        fingerprint = self._build_fingerprint(request)
        lock_key = f"dup_post_lock:{fingerprint}"
        redirect_key = f"dup_post_redirect:{fingerprint}"

        if not cache.add(lock_key, True, timeout=self.LOCK_TIMEOUT_SECONDS):
            target = cache.get(redirect_key) or request.headers.get("Referer") or request.path
            return HttpResponseRedirect(target)

        response = self.get_response(request)

        if 300 <= response.status_code < 400 and "Location" in response:
            cache.set(redirect_key, response["Location"], timeout=self.LOCK_TIMEOUT_SECONDS)
        else:
            cache.delete(lock_key)

        return response

    def _build_fingerprint(self, request) -> str:
        """Create a deterministic SHA-256 fingerprint for a POST request."""
        if getattr(request, "user", None) and request.user.is_authenticated:
            actor = f"user:{request.user.pk}"
        elif getattr(request, "session", None) and request.session.session_key:
            actor = f"session:{request.session.session_key}"
        else:
            actor = f"ip:{request.META.get('REMOTE_ADDR', '')}"

        items = sorted(
            (key, values)
            for key, values in request.POST.lists()
            if key != "csrfmiddlewaretoken"
        )
        raw = json.dumps([actor, request.path, items], sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()
