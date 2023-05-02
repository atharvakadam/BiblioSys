import random
from rewards import Rewards
class DiscountRewards(Rewards):
    def __init__(self):
        self.available_rewards = [  "5% discount at select grocery outlets",
                                    "5% discount at gas stations",
                                    "10% discount at select bookstores",
                                    "5% discount on any Amazon.com purchases above $100", 
                                    "7% discount on select restaurants",
                                ]
        
    def issue_reward(self):
        reward_coupon = random.choice(self.available_rewards)
        return reward_coupon