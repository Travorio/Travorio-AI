import aiohttp

from gemini2_travel_v2 import FlightRequest


# Define the async function to call Travorio API
async def travorio_search_flights(flight_request: FlightRequest):
    """
    Searches flights using the Travorio Flight Search API.

    Args:
        flight_request (FlightRequest): Object containing flight search details.

    Returns:
        dict: Flight search results from Travorio API.
    """
    # Travorio API endpoint
    api_url = "https://staging-api.travorio.com/api/v1/flight-search"

    # Define the headers (you may need a token/API key)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijk5ZDU2MjU2LThiZmUtNGRhYi1hNDEyLTk2ZmExYzZmMDBlYiIsImVtYWlsIjoidHJhdm9yaW8tYWRtaW5AZ21haWwuY29tIiwidXNlcm5hbWUiOiJBZG1pbiBVc2VyIiwiZmlyc3ROYW1lIjoiQWRtaW4iLCJwaG9uZSI6Ijk4ODg4ODg4ODgiLCJsYXN0TmFtZSI6IlVzZXIiLCJ1c2VyVHlwZSI6MiwiaXNBY3RpdmUiOnRydWUsInBob25lQ291bnRyeUNvZGUiOiIxIiwiZG9iIjpudWxsLCJpc0VtYWlsVmVyaWZpZWQiOnRydWUsImNvdW50cnkiOm51bGwsInByb2ZpbGVQaWMiOiIxNzM5NDM2NTE1MjEyLmpwZWciLCJwcmVmZXJyZWRMYW5ndWFnZSI6IiIsImlhdCI6MTc0Mzk3NDY4NCwiZXhwIjoxNzQ0MjMzODg0fQ._jf5HJZkNJTBRkdR7FvVJLBhh4U0HP_0kO7vhXCxWcM"  # AUTH via GEMINI_API_KEY
    }

    # Create the API payload based on the FlightRequest fields
    payload = {
        "origin": flight_request.origin,
        "destination": flight_request.destination,
        "outboundDate": flight_request.outbound_date,
        "returnDate": flight_request.return_date
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(api_url, json=payload, headers=headers) as response:
                if response.status == 200:
                    return await response.json()  # Parse JSON response
                else:
                    logger.error(f"Travorio API Error: {response.status} - {response.reason}")
                    return {
                        "error": f"API call failed with status {response.status}: {await response.text()}"
                    }
    except Exception as e:
        logger.exception("An exception occurred while searching for flights")
        return {"error": str(e)}
