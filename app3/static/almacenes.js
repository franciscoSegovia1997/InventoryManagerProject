function consultarUsuariosxAlmacen(idAlmacen)
{
    console.log(idAlmacen)
    fetch(`/consultaAlmacen/${idAlmacen}`)
    .then(response => response.json())
    .then(data => {
        nombreAlmacenUsuarios = document.getElementById('nombreAlmacenUsuarios')
        nombreAlmacenUsuarios.innerHTML = data.nombreAlmacen
        usuariosxalmacen = document.getElementById('usuariosxalmacen')
        usuariosxalmacen.innerHTML = ''
        for(let i = 0; i < data.lista_usuarios.length; i++)
        {
            usuariosxalmacen.innerHTML += `
            <tr>
                <td>${data.lista_usuarios[i][0]}</td>
                <td>${data.lista_usuarios[i][1]}</td>
                <td>${data.lista_usuarios[i][2]}</td>
            </tr>
            `
        }
    })
}