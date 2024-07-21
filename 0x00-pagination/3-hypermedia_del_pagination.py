#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict[str, Any]:
        """
        Get a page of the dataset with given start index and page size,
        resilient to deletions.

        Args:
            index (int): The starting index of the page (default None).
            page_size (int): The number of items per page (default 10).

        Returns:
            Dict[str, Any]: A dictionary containing pagination information.
        """
        assert index is not None and isinstance(index, int)
        assert 0 <= index < len(self.dataset())
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        data = []
        next_index = index

        for _ in range(page_size):
            while (next_index not in indexed_data and
                   next_index < len(self.dataset())):
                next_index += 1
            if next_index >= len(self.dataset()):
                break
            data.append(indexed_data[next_index])
            next_index += 1

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': (next_index if next_index < len(self.dataset())
                           else None)
        }


# Main for testing the method
if __name__ == "__main__":
    server = Server()
    server.indexed_dataset()

    try:
        server.get_hyper_index(300000, 100)
    except AssertionError:
        print("AssertionError raised when out of range")

    index = 3
    page_size = 2

    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 1- request first index
    res = server.get_hyper_index(index, page_size)
    print(res)

    # 2- request next index
    print(server.get_hyper_index(res.get('next_index'), page_size))

    # 3- remove the first index
    del server._Server__indexed_dataset[res.get('index')]
    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 4- request again the initial index -> the first data retrieves
    #    is not the same as the first request
    print(server.get_hyper_index(index, page_size))

    # 5- request again initial next index -> same data page as request 2-
    print(server.get_hyper_index(res.get('next_index'), page_size))
