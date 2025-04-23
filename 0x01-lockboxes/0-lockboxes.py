#!/usr/bin/python3
"""Lockboxes module"""
from queue import Queue


def canUnlockAll(boxes):
    """Lockboxes implementation"""
    n = len(boxes)

    checked_boxes = [False] * n
    checked_boxes[0] = [True]

    queue = [0]

    while queue:
        box = queue.pop()
        for key in boxes[box]:
            if key < n and not checked_boxes[key]:
                checked_boxes[key] = True
                queue.append(key)

    return all(checked_boxes)
