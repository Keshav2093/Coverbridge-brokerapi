class PolicyService:
    """
    Core Policy Administration System
    """
    def create_policy(self, user_id: str, plan_id: str) -> str:
        # Mock policy creation
        return f"POL-{user_id[:4].upper()}-8899"

    def get_policy(self, policy_id: str) -> dict:
        return {"id": policy_id, "status": "Active"}

policy_service = PolicyService()
