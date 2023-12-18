function App()
{
    function getCookie(name)
    {
        let cookieValue = null;
        if(document.cookie && document.cookie !== "")
        {
            const cookies = document.cookie.split(';');
            for(let i = 0; i < cookies.length; i++)
            {
                const cookie = cookies[i].trim();
                if(cookie.substring(0,name.length + 1) === (name + "="))
                {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue 
    }

    const [state,setState] = React.useState({
        productoSeleccionado:{
            id:'',
            nombre:'',
            codigo:'',
            precio:'',
            cantidad:'',
        },
        productosSeleccion:[],
        productosCoti:[],
        nombreCliente:'',
        documentoCliente:'',
    });

    React.useEffect(()=>{
        fetch('/consultarProductos')
        .then(response => response.json())
        .then(data => {
            const listaSeleccion = data.listaProductos.map(productoInfo => ({
                id:productoInfo[0],
                nombre:productoInfo[1],
                codigo:productoInfo[2],
                precio:productoInfo[3]
            }));
            setState((prevState) => ({
                ...prevState,
                productosSeleccion: listaSeleccion,
            }));
        })
        .catch(error => {
            console.error('Error al cargar los productos')
        })
    },[])

    const seleccionarProducto = (event) =>{
        const productoId = event.target.value;
        const productoInformacion = state.productosSeleccion.find(producto => producto.id === productoId);
        if(productoInformacion){
            setState((prevState) => ({
                ...prevState,
                productoSeleccionado:{
                    id:productoInformacion.id,
                    nombre:productoInformacion.nombre,
                    codigo:productoInformacion.codigo,
                    precio:productoInformacion.precio,
                    cantidad:'0',
                }
            }));
        }
    }

    const cambiarNombreCliente = (event) => {
        const nuevoNombre = event.target.value;
        setState((prevState) => ({
            ...prevState,
            nombreCliente:nuevoNombre,
        }));
    }

    const cambiarDocumentoCliente = (event) => {
        const nuevoDocumento = event.target.value;
        setState((prevState) => ({
            ...prevState,
            documentoCliente:nuevoDocumento,
        }));
    }


    const cambiarPrecio = (event) => {
        const nuevoPrecio = event.target.value;
        setState((prevState) => ({
            ...prevState,
            productoSeleccionado:{
                id:state.productoSeleccionado.id,
                nombre:state.productoSeleccionado.nombre,
                codigo:state.productoSeleccionado.codigo,
                precio:String(nuevoPrecio),
                cantidad:state.productoSeleccionado.cantidad,
            }
        }));
    }

    const cambiarCantidad = (event) => {
        const nuevaCantidad = event.target.value;
        setState((prevState) => ({
            ...prevState,
            productoSeleccionado:{
                id:state.productoSeleccionado.id,
                nombre:state.productoSeleccionado.nombre,
                codigo:state.productoSeleccionado.codigo,
                precio:state.productoSeleccionado.precio,
                cantidad:String(nuevaCantidad),
            }
        }));
    }

    const agregarProducto = (event) => {
        if(state.productoSeleccionado.id !== '')
        {
            setState((prevState) => ({
                ...prevState,
                productosCoti:[
                    ...state.productosCoti,
                    state.productoSeleccionado
                ]
            }));
            setState((prevState) => ({
                ...prevState,
                productoSeleccionado:{
                    id:'',
                    nombre:'',
                    codigo:'',
                    precio:'',
                    cantidad:'0',
                }
            }));
        }
    }

    const eliminarProducto = (id) =>{
        const nuevosProductosCoti = state.productosCoti.filter((producto) => producto.id !== id);
        setState((prevState) => ({
            ...prevState,
            productosCoti: nuevosProductosCoti,
        }));
    }

    const crearCoti = () => {

        const cotizacionData = {
            productosCoti: state.productosCoti,
            nombreCliente: state.nombreCliente,
            documentoCliente: state.documentoCliente
        }
        fetch('/crearCotizacion',{
            method:"POST",
            headers:{
                "X-Requested-With":"XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body:JSON.stringify(cotizacionData)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            window.location.href = '/cotizaciones';
        })
        .catch(error => {
            console.error("Error al crear cotizacion", error)
        });
    }


    const estilosContenedor = {
        height: '100vh',
        overflow: 'scroll'
    };


    return(
        <div className="container" style={estilosContenedor}>
            <h1 className="mt-3 mb-3">Crear cotizacion</h1>
            <br />
            <div>
                <div className='row mb-3 mt-3'>
                <div className="col-6">
                        <label>Cliente</label>
                        <input type="text" className="form-control" value={state.nombreCliente} onChange={cambiarNombreCliente}/>
                    </div>
                    <div className="col-6">
                        <label>Documento</label>
                        <input type="text" className="form-control" value={state.documentoCliente} onChange={cambiarDocumentoCliente}/>
                    </div>
                </div>


                <div className="row mb-3 mt-3">
                    <div className="col-6">
                        <label>Seleccionar producto</label>
                        <select className='form-select' onChange={seleccionarProducto}>
                            <option value=''></option>
                            {
                                state.productosSeleccion.map((producto)=>(
                                    <option key={producto.id} value={producto.id}>{producto.nombre}</option>
                                ))
                            }
                        </select>
                    </div>
                </div>
                <div className='row mb-3 mt-3'>
                    <div className="col-6">
                        <label>Nombre</label>
                        <input type="text" className="form-control" value={state.productoSeleccionado.nombre} readOnly/>
                    </div>
                    <div className="col-6">
                        <label>Codigo</label>
                        <input type="text" className="form-control" value={state.productoSeleccionado.codigo} readOnly/>
                    </div>
                </div>
                <div className='row mb-3 mt-3'>
                    <div className="col-6">
                        <label>Precio</label>
                        <input type="text" className="form-control" value={state.productoSeleccionado.precio} onChange={cambiarPrecio} />
                    </div>
                    <div className="col-6">
                        <label>Cantidad</label>
                        <input type="number" className="form-control" value={state.productoSeleccionado.cantidad} onChange={cambiarCantidad} />
                    </div>
                </div>
                <div className='row mb-3 mt-3'>
                    <div className="col-2">
                        <br />
                        <button className='btn btn-success' onClick={agregarProducto}>Agregar</button>
                    </div>
                </div>
            </div>



            <br />
            <div>
                <table className="table table-bordered table-hover">
                    <thead className="table-dark">
                        <tr>
                            <th>Nombre</th>
                            <th>Codigo</th>
                            <th>Precio</th>
                            <th>Cantidad</th>
                            <th>Eliminar</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            state.productosCoti.map((producto) => (
                                <tr key={producto.id}>
                                    <td>{producto.nombre}</td>
                                    <td>{producto.codigo}</td>
                                    <td>{producto.precio}</td>
                                    <td>{producto.cantidad}</td>
                                    <td className='text-center'><button className='btn btn-danger' onClick={() => eliminarProducto(producto.id)}>D</button></td>
                                </tr>
                            ))
                        }
                    </tbody>
                </table>
            </div>
            <div className='row mb-3 mt-3'>
                <div className='col-2'>
                    <a className='btn btn-secondary' href="/cotizaciones">Cancelar</a>
                </div>
                <div className='col-2'>
                    <button className='btn btn-primary' onClick={crearCoti}>Crear</button>
                </div>
            </div>
        </div>
    );
}