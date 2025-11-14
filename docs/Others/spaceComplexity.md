---
title: 空間複雜度
parent: Others
---

# 空間複雜度
空間複雜度（Space Complexity）是衡量演算法所需記憶體空間的度量。

## 基本概念

1. **基本記憶體需求**：如基本資料類型（整數、浮點數、布林值等）的儲存。
2. **額外空間**：如儲存資料結構（如陣列、鏈表、堆疊、隊列等）。

## 大O表示法（Big-O notation）

- **O(1)**：常數空間，表示無論輸入大小如何，所需的空間始終保持固定。例如，只用到少數變數來儲存結果。
- **O(n)**：線性空間，表示空間需求與輸入的大小成正比。常見的例子是儲存一個大小為 `n` 的陣列或列表。
- **O(n^2)**：平方空間，表示空間需求與輸入大小的平方成正比。像是儲存一個 `n x n` 的矩陣。
- **O(log n)**：對數空間，表示空間需求是輸入大小的對數量級，通常發生在分治演算法中，像是二分搜尋的遞迴過程。

## 如何計算？

1. 考慮資料結構的空間。
2. **遞迴的額外空間**：遞迴演算法需要額外的堆疊空間來儲存每次函式調用的狀態。

## 範例

1. **線性搜尋**（O(n) 空間複雜度）：

    ```
    function linearSearch(arr, target) {
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] === target) {
                return i;
            }
        }
        return -1;
    }
    ```

    這段程式碼的空間複雜度是 O(1)，因為它只是用了一些基本變數（`i` 和 `target`），並沒有額外的資料結構。

    ```
    function findMax(arr) {
        let maxVal = -Infinity; // 只使用一個變數
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] > maxVal) {
                maxVal = arr[i]; // 更新最大值
            }
        }
        return maxVal;
    }

    console.log(findMax([3, 1, 4, 1, 5, 9])); // 9
    ```

    - 無論 `arr` 多大，我們**只使用一個變數** **`maxVal`**，不會開額外的陣列或資料結構來存資料。
    - 空間使用是**固定的**，不會隨著 `n` 增長而改變，因此空間複雜度是 **O(1)**。

2. （O(n) 空間複雜度）：
    ```
    function copyArray(arr) {
        let newArr = []; // 建立一個新的陣列
        for (let i = 0; i < arr.length; i++) {
            newArr.push(arr[i]); // 複製每個元素到新的陣列
        }
        return newArr;
    }

    const original = [1, 2, 3, 4, 5];
    const copied = copyArray(original);
    console.log(copied); // [1, 2, 3, 4, 5]
    ```

    - `newArr` 會存放與 `arr` 相同數量的元素，佔用的額外記憶體空間是 `n`。
    - 這代表隨著 `arr` 的長度增加，`newArr` 也會等比例增加，因此空間複雜度是 **O(n)**。

3. **O(n^2)：**平方空間
    ```
    function generatePairs(arr) {
        let pairs = [];
        for (let i = 0; i < arr.length; i++) {
            for (let j = 0; j < arr.length; j++) {
                pairs.push([arr[i], arr[j]]);
            }
        }
        return pairs;
    }

    console.log(generatePairs([1, 2, 3]));
    /*
    [
    [1, 1], [1, 2], [1, 3],
    [2, 1], [2, 2], [2, 3],
    [3, 1], [3, 2], [3, 3]
    ]
    */
    ```

    - `pairs` 陣列儲存了 **所有元素兩兩配對**，總共有 `n × n` 個組合。
    - 隨著 `n` 增加，配對數量以平方級增長，因此空間複雜度是 **O(n²)**。

4. **O(log n)**：對數空間

    表示演算法的額外空間需求**隨著輸入** **`n`** **增長，而以對數級數增加**，而不是線性或平方級成長。這通常出現在**遞迴演算法（如二分搜尋）或某些樹形結構的操作**中。

    二分搜尋（Binary Search）：

    ```
    function binarySearch(arr, target, left = 0, right = arr.length - 1) {
        if (left > right) return -1; // 找不到目標值

        let mid = Math.floor((left + right) / 2);

        if (arr[mid] === target) return mid;
        else if (arr[mid] > target) return binarySearch(arr, target, left, mid - 1);
        else return binarySearch(arr, target, mid + 1, right);
    }

    console.log(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)); // 4
    ```

    二分搜尋每次都把搜尋範圍**縮小一半**，如果使用**遞迴**來實作，則遞迴深度最多是 `log n`，因此空間複雜度是 O(log n)。

    - 每次遞迴時，我們只需記住**當前的搜尋範圍**（`left` 和 `right`），不會額外儲存所有元素。
    - 遞迴深度最多是 **log₂(n)**，所以空間複雜度是 **O(log n)**。
    - **如果改用迴圈來實作二分搜尋，則空間複雜度變為 O(1)。**

    二元樹的遞迴遍歷：

    ```
    class TreeNode {
        constructor(value) {
            this.value = value;
            this.left = null;
            this.right = null;
        }
    }
    // 測試樹
    let root = new TreeNode(4);
    root.left = new TreeNode(2);
    root.right = new TreeNode(6);
    root.left.left = new TreeNode(1);
    root.left.right = new TreeNode(3);
    root.right.left = new TreeNode(5);
    root.right.right = new TreeNode(7);
    /*

         4
       /  \
      2    6
     / \  / \
    1  3  5  7

    */
    ```

    - 在**平衡二元樹**（如 AVL、紅黑樹）中，樹的高度為 `log n`。
    - 遞迴函式的**最大呼叫深度**是樹的高度，也就是 `O(log n)`。
    - **每次遞迴只需額外的函式呼叫棧，而不需要額外的陣列儲存數據。**

    ⚠ **注意：如果樹是線性結構（退化成鏈表），空間複雜度就會變成 O(n)。**

    快速排序（Quick Sort）- 最佳情況：

    ```
    function quickSort(arr) {
        if (arr.length <= 1) return arr;

        let pivot = arr[Math.floor(arr.length / 2)];
        let left = arr.filter(x => x < pivot);
        let middle = arr.filter(x => x === pivot);
        let right = arr.filter(x => x > pivot);

        return [...quickSort(left), ...middle, ...quickSort(right)];
    }

    console.log(quickSort([3, 1, 4, 1, 5, 9, 2, 6, 5]));
    // [1, 1, 2, 3, 4, 5, 5, 6, 9]
    ```

    - **每次遞迴時，會將陣列分成兩半**，最多會有 `log n` 層的遞迴呼叫。
    - **遞迴深度決定了額外的空間使用量**，在平均情況下是 `log n`，所以空間複雜度是 **O(log n)**。

    ⚠ **注意：如果每次選到的 pivot 讓陣列分割得很不均勻（最差情況），遞迴深度可能會變成 O(n)。**

---

## 技巧

- **忽略常數項**：當空間需求與輸入規模成正比時，只考慮最高次的項目（例如 O(n + 1000) 與 O(n) 等價）。
- **合併空間需求**：如果演算法中有多個步驟，每個步驟的空間需求可以合併，通常會選擇最壞情況下的空間需求。