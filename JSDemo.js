let list1 = [1, 2, 3, 5, 6, 8, 9];

function search(list1, num) {
  for (let i = 0; i < list1.length; i++) {
    if (num === list1[i]) {
      return "We found the number ";
    }
  }
  return "Not found !!";
}
console.log(search(list1, 5));
