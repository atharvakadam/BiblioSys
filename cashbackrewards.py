import random
from rewards import Rewards
class CashbackRewards(Rewards):
    def __init__(self):
        self.available_rewards = [  "5% cashback at select grocery outlets for 1 month",
                                    "5% cashback at gas stations for 1 month",
                                    "10% cashback at select bookstores",
                                    "5% cashback on any Amazon.com purchases above $100", 
                                    "7% cashback on select restaurants",
                                ]
        
    def issue_reward(self):
        reward_coupon = random.choice(self.available_rewards)
        return reward_coupon