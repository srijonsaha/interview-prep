# Interview Prep

## Big-O Complexity

$O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)$

## Hash Table

```js
const map = new Map();

map.set("key1", "value1");
map.set("key2", "value2");
map.has("key1"); // true
map.get("key1"); // "value1"
```

## Linked List

```js
class Node {
    constructor(data, next = null) {
        this.data = data;
        this.next = next;
    }
}

class LinkedList {
    constructor(head = null) {
        this.head = head;
    }

    insertAtBeginning(data) {
        let newNode = new Node(data);
        newNode.next = this.head;
        this.head = newNode;
        return this.head;
    }

    insertAtEnd(data) {
        let newNode = new Node(data);
        if (!this.head) {
            this.head = newNode;
            return this.head;
        }
        let tail = this.head;
        while (tail.next !== null) {
            tail = tail.next;
        }
        tail.next = newNode;
        return this.head;
    }
}
```

## Stack

```js
const stack = [];
stack.push("item");
stack.pop();
stack[stack.length - 1]; // peek top of stack
```

## Queue

```js
const queue = [];
queue.push("item"); // enqueue
queue.shift(); // dequeue
queue[0]; // peek top of queue
```

## Binary Search

### Iteration Method

```js
function binarySearch(arr, key) {
    let start = 0;
    let end = arr.length - 1;

    while (start <= end) {
        const mid = Math.floor((start + end) / 2);

        if (arr[mid] === key) {
            return mid;
        }

        if (arr[mid] > key) {
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }
    return -1;
}
```

### Recursive Method

```js
function binarySearch(arr, key, start = 0, end = arr.length - 1) {
    if (start > end) {
        return -1;
    }

    const mid = Math.floor((start + end) / 2);

    if (arr[mid] === key) {
        return mid;
    }

    return arr[mid] > key
        ? binarySearch(arr, key, start, mid - 1)
        : binarySearch(arr, key, mid + 1, end);
}
```

## Trees

```js
class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}
```

### In-Order Traversal

```js
function inOrderTraversal(node) {
    if (node !== null) {
        inOrderTraversal(node.left);
        console.log(node.value);
        inOrderTraversal(node.right);
    }
}
```

### Pre-Order Traversal

```js
function preOrderTraversal(node) {
    if (node !== null) {
        console.log(node.value);
        preOrderTraversal(node.left);
        preOrderTraversal(node.right);
    }
}
```

### Post-Order Traversal

```js
function postOrderTraversal(node) {
    if (node !== null) {
        postOrderTraversal(node.left);
        postOrderTraversal(node.right);
        console.log(node.value);
    }
}
```

## Graph

```js
class Node {
    constructor(value) {
        this.value = value;
        this.children = [];
    }
}
```

### Breadth First Search

```js
function bfs(root) {
    const result = [];
    const queue = [root];
    const visited = new Set();

    while (queue.length > 0) {
        const curr = queue.shift();

        if (!visited.has(curr)) {
            result.push(curr.value);

            for (const child of curr.children) {
                queue.push(child);
            }
            visited.add(curr);
        }
    }
    return result;
}
```

### Depth First Search

```js
function dfs(root) {
    const result = [];
    const stack = [root];
    const visited = new Set();

    while (stack.length > 0) {
        const curr = stack.pop();

        if (!visited.has(curr)) {
            result.push(curr.value);

            for (const child of curr.children) {
                stack.push(child);
            }
            visited.add(curr);
        }
    }
    return result;
}
```
