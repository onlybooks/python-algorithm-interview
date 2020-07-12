// Go
func twoSum(nums []int, target int) []int {
    numsMap := make(map[int]int)

    // 키와 값을 바꿔서 딕셔너리로 저장
    for i, num := range nums {
        numsMap[num] = i
    }

    // 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num := range nums {
        if j, ok := numsMap[target-num]; ok && i != j {
            return []int{i, j}
        }
    }

    return []int{}
}