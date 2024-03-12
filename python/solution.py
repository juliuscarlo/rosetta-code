# datatype
import random
from threading import Thread, Lock


class BucketSet:
    def __init__(self, starting_values: tuple) -> None:
        self.buckets = list(starting_values)
        self.mutex = Lock()

    def get_bucket_value(self, bucket_id):
        return self.buckets[bucket_id]

    def update_value(self, bucket_index, value):
        self.buckets[bucket_index] = value

    def transfer_content(self, donor_index: int, receiver_index: int, value) -> None:
        # this should be an atomic operation
        with self.mutex:
            donor_value_old = self.get_bucket_value(donor_index)
            receiver_value_old = self.get_bucket_value(receiver_index)

            # Make sure donor does not give more than they have
            transfer_amount = value if value <= donor_value_old else donor_value_old

            donor_value_new = donor_value_old - transfer_amount
            receiver_value_new = receiver_value_old + transfer_amount
            self.update_value(bucket_index=donor_index, value=donor_value_new)
            self.update_value(bucket_index=receiver_index, value=receiver_value_new)

    def check_bucket_state(self):
        return self.buckets

    def pick_random_bucket_index_pair(self) -> list:
        return random.sample(range(len(self.buckets)), 2)

    def redistribute_bucket_pair_contents(self, bucket_index_pair: list) -> None:
        donor_index, receiver_index = random.sample(bucket_index_pair, 2)
        transfer_amount = random.randint(
            0, self.get_bucket_value(bucket_id=donor_index)
        )
        self.transfer_content(
            donor_index=donor_index,
            receiver_index=receiver_index,
            value=transfer_amount,
        )

    def equalize_bucket_pair(self, bucket_index_pair: list) -> None:
        donor_index, receiver_index = random.sample(bucket_index_pair, 2)
        # pick the bucket with more contents and transfer ~1/2 of that to the other bucket


def main():
    # create a set of buckets and start 3 concurrent tasks
    starting_values = (100, 5, 50, 7, 33)
    buckets = BucketSet(starting_values=starting_values)

    # Run the experiment for 10 seconds, so set some kind of termination signal for the threads to stop

    # Start the threads

    # 1) as often as possible, pick 2 buckets and make their values closer to equal
    buckets.redistribute_bucket_pair_contents()

    # 2) as often as possible, pick 2 buckets and arbitrarily redistribute their values
    buckets.equalize_bucket_pair()

    # 3) display the total value and (optionally) the in dividual values of each bucket
    # Make a loop that prints the bucket contents every second
