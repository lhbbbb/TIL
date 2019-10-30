# Input 태그 input 값 핸들링 하기

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <h1>My Shopping List</h1>
  Enter a new item: <input id="item-input" type="text">
  <button id="add-button">Add Item</button>
  <ul id="shopping-list">

  </ul>

  <script>
    const input = document.querySelector('#item-input')
    const button = document.querySelector('#add-button')
    const shoppingList = document.querySelector('#shopping-list')
    button.addEventListener('click', e => {
      const itemName = input.value
      input.value = ''
      const item = document.createElement('li')
      item.innerText = itemName
      
      shoppingList.appendChild(item)
    })
  </script>
</body>
</html>
```

* SPA(Single Page Application)



# JavaScript API 사용하기

