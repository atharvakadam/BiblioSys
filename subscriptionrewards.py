import random
from rewards import Rewards
class SubscriptionRewards(Rewards):
    def __init__(self):
        self.available_rewards = [  "Apple Music Subscription - 2 months",
                                    "Spotify Subscription - 3 months",
                                    "Netflix Subscription - 1 month",
                                    "Prime Video Subscription - 3 months", 
                                    "HBOMax Subscription - 1 month",
                                ]
        
    def issue_reward(self):
        reward_coupon = random.choice(self.available_rewards)
        return reward_coupon