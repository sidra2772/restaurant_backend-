from django.utils.deprecation import MiddlewareMixin

class GHLTokenMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """
        Attach tokens from session to request
        """
        access_token = request.session.get("ghl_access_token")
        refresh_token = request.session.get("ghl_refresh_token")
        company_id = request.session.get("ghl_company_id")
        location_id = request.session.get("ghl_location_id")
        user_id = request.session.get("ghl_user_id")

        request.access_token = access_token
        request.refresh_token = refresh_token
        request.company_id = company_id
        request.location_id = location_id
        request.user_id = user_id
