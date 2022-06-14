const url = 'https://fakestoreapi.com/products';
$(document).ready(
    function() 
    {
        $.get(url, 
            function(jsonObj)
            {
                
                const data = jsonObj;
                var arrLen = data.length;
                console.log(data);
                for (var i = 0; i < 6; i++)
                {
                    fillProduct(data, 'comida-' + (i + 1).toString(), i);
                }
            })
    }
)

function fillProduct(data, id, index)
{
    var productInfo = data[index];
    document.getElementById(id).innerHTML = productInfo['title'];
    document.getElementById(id + '-desc').innerHTML = productInfo['description'];
    document.getElementById(id + '-price').innerHTML += productInfo['price'];
    document.getElementById(id + '-image').src = productInfo['image'];
}