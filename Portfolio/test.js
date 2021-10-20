const withdraw = amount => {

  let amt = amount;
  let test_amt = [100,50,20];
  let arr = [];
  count = 0
  if(amt < 40 && amt > 1000) return [];
  for(let val of test_amt){
    let qoutient = Math.floor(amt/val)
    data = amt % val
    if(count > 0){
      arr.push(data)
    }
    arr.push(qoutient);
    count++
  }
  return arr;
};

console.log(withdraw(250))