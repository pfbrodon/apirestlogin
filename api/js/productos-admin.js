const { createApp } = Vue
createApp({
    data() {
        return {
            productos: [],
            //url:'http://localhost:5000/productos', 
            // si el backend esta corriendo local  usar localhost 5000(si no lo subieron a pythonanywhere)
            url: 'https://yoti.pythonanywhere.com/productos', // si ya lo subieron a pythonanywhere
            error: false,
            cargando: true,
            /*atributos para el guardar los valores del formulario */


            id: 0,
            nombre: "",
            imagen: "",
            precio: 0,
            stock: 0,
            descripcion: "",
            categoria: "",
            busqueda: "",
            productosFiltrados: [],

        }
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    this.productos = data;
                    this.cargando = false
                })
                .catch(err => {
                    console.error(err);
                    this.error = true
                })
        },
        eliminar(id) {
            const url = this.url + '/' + id;
            var options = {
                method: 'DELETE',
            }
            fetch(url, options)
                .then(res => res.text()) // or res.json()
                .then(res => {
                    alert('Registro Eliminado')
                    location.reload(); // recarga el json luego de eliminado el registro
                })
        },
        grabar() {
            let producto = {
                nombre: this.nombre,
                imagen: this.imagen,
                precio: this.precio,
                stock: this.stock,
                descripcion: this.descripcion,
                categoria: this.categoria

            }
            var options = {
                body: JSON.stringify(producto),
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url, options)
                .then(function() {
                    alert("Registro grabado")
                    window.location.href = "../html/admin.html"; // recarga productos.html
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Grabar") // puedo mostrar el error tambien
                })
        },

        filtrarProductos() {
            this.productosFiltrados = this.productos.filter(producto => {
                const busquedaLowerCase = this.busqueda.toLowerCase();

                // Verificar si la búsqueda tiene un formato específico para filtrar
                // por propiedades. Ejemplo de busqueda = "cat:tarugos"
                if (busquedaLowerCase.startsWith('id:')) {
                    const id = producto.id.toString().toLowerCase();
                    return id.includes(busquedaLowerCase.substring(3));
                } else if (busquedaLowerCase.startsWith('desc:')) {
                    const descripcion = producto.descripcion.toLowerCase();
                    return descripcion.includes(busquedaLowerCase.substring(5));
                } else if (busquedaLowerCase.startsWith('cat:')) {
                    const categoria = producto.categoria.toLowerCase();
                    return categoria.includes(busquedaLowerCase.substring(4));
                } else if (busquedaLowerCase.startsWith('precio:')) {
                    const precio = producto.precio.toString().toLowerCase();
                    return precio.includes(busquedaLowerCase.substring(7));
                } else {
                    // Si no se proporciona un comando específico, buscar por nombre
                    return (
                        producto.nombre.toLowerCase().includes(busquedaLowerCase)
                    );
                }
            });
        }

    },
    created() {
        this.fetchData(this.url)
    },
}).mount('#app')