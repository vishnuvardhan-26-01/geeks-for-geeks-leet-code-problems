class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next

        position = 1

        first = -1
        last = -1
        minDistance = float('inf')

        while curr.next:
            next_node = curr.next

            # Check if curr is a critical point
            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):

                if first == -1:
                    # First critical point
                    first = position
                else:
                    # Distance from previous critical point
                    minDistance = min(minDistance, position - last)

                last = position

            prev = curr
            curr = next_node
            position += 1

        # Fewer than two critical points
        if first == -1 or first == last:
            return [-1, -1]

        maxDistance = last - first

        return [minDistance, maxDistance]