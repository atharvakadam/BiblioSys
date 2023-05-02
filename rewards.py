from abc import ABCMeta, abstractmethod        
"""
Rewards class -> Custom rewards that can be created by the library for special members
Could write this class as an interface instead and implement different rewards classes
"""
class Rewards(metaclass=ABCMeta):
    """An interface for reward systems.
    
    This interface defines a method for issuing rewards to special members in a library system.
    The `issue_reward()` method should be implemented by any class that inherits from this interface.
    """
    
    @abstractmethod
    def issue_reward(self) -> str:
        """Issues a reward to a special member.
        
        This method should be implemented by any class that inherits from this interface.
        
        Returns:
            A string representing the reward that has been issued.
        """
        pass
