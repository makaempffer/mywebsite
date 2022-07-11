const url = 'http://127.0.0.1:8000/api/ofertas';
$(document).ready(
    function() 
    {
        $.get(url, 
            function(data)
            {
                console.log(data, data.length);
                if (data.length > 0) {
                    data.forEach( (v, i, a) => {
                        $('#tabla-ofertas > tbody:last-child').append(`<tr><td>${v.nombre}</td><td>${v.descripcion}</td><td>${v.vigente ? 'Vigente' : 'Caducada'}</td></tr>`)
                    });
                } else {
                    $('#tabla-ofertas > tbody:last-child').append(`<tr><td>-</td><td>SIN INFORMACIÓN</td><td>-</td></tr>`);
                }
            })
    }
)