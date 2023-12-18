document.addEventListener('DOMContentLoaded',()=>{
    numeroEspecial = document.getElementById('numeroEspecial')
    numeroEspecial.innerHTML = '243'
})

function incrementarNumero()
{
    numeroIncrementar = document.getElementById('numeroEspecial')
    nuevoNumero = Number(numeroIncrementar.innerHTML) + 1
    numeroIncrementar.innerHTML = String(nuevoNumero)
}

function disminuirNumero()
{
    numeroDisminuir = document.getElementById('numeroEspecial')
    nuevoNumero = Number(numeroIncrementar.innerHTML) - 1
    numeroDisminuir.innerHTML = String(nuevoNumero)
}

function imprimirSeleccion()
{
    numeroSeleccionado = document.getElementById('numeroSeleccionado')
    console.log(`El numero seleccionado es : ${numeroSeleccionado.value}`)
    nuevoNumero = document.getElementById('nuevoNumero')
    nuevoNumero.value = numeroSeleccionado.value
}

function agregarNumero()
{
    valorNumero = document.getElementById('nuevoNumero')
    listaNumeros = document.getElementById('listaNumeros')
    listaNumeros.innerHTML += `
        <li class='numeroSuma'>${valorNumero.value}</li>
    `
}

function actualizarSuma()
{
    arregloNumeros = document.querySelectorAll('.numeroSuma')
    let sumaTotal = 0
    for(let i=0; i < arregloNumeros.length; i++)
    {
        numTemp = Number(arregloNumeros[i].innerHTML)
        sumaTotal = sumaTotal + numTemp
    }
    sumaFinal = document.getElementById('sumaFinal')
    sumaFinal.innerHTML = String(sumaTotal)
}