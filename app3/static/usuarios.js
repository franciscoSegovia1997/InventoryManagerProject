function cargarUsuario(idUsuario)
{
    fetch(`/consultaUsuario/${idUsuario}`)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        editarUsername = document.getElementById('editarUsername')
        editarNombre = document.getElementById('editarNombre')
        editarApellido = document.getElementById('editarApellido')
        editarEmail = document.getElementById('editarEmail')
        editarRol = document.getElementById('editarRol')
        editarId = document.getElementById('editarId')

        editarUsername.value = data.usernameUsuario
        editarNombre.value = data.nombreUsuario
        editarApellido.value = data.apellidoUsuario
        editarEmail.value = data.emailUsuario
        editarRol.value = data.rolUsuario
        editarId.value = data.idUsuario
    })
}