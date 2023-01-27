from behavioral_patterns.observer.publisher import *
from behavioral_patterns.observer.subscriber import *


if __name__ == '__main__':
    # The client code.

    publisher = ConcretePublisher()

    subscriber_a = ConcreteSubscriberA()
    publisher.attach(subscriber_a)

    subscriber_b = ConcreteSubscriberB()
    publisher.attach(subscriber_b)

    publisher.some_business_logic()
    publisher.some_business_logic()

    publisher.detach(subscriber_a)

    publisher.some_business_logic()
    
    