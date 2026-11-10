func isPalindrome(x int) bool {

    temp := x
    dig := 0

    for temp > 0{
        rem := temp % 10
        dig = (dig*10)+rem
        temp = temp / 10
    }

    if x == dig{
        return true
    }

    return false
    
}