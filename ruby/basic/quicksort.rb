num = [1, 3, 2, 8, 0, 7]

def quicksort num 
    less, larger = [], []
    if num.length <= 1 then return num end 
    pivot = num.pop 
    num.each do |i| if i <= pivot then less.push i else larger.push i end end
    quicksort(less) + [pivot] + quicksort(larger)
end

puts quicksort num


