console.log(location.search) // lee los argumentos pasados a este formulario
var id = location.search.substr(4) // producto_update.html?id=1
console.log(id)
const { createApp } = Vue
createApp({
    data() {
        return {
            id: 0,
            categoria: "",
            codigo: 0,
            descripcion: "",
            cantidad: 0,
            precioUnit: 0,
            precioVPublico: 0,
            url: 'https://pfbrodon.pythonanywhere.com/productos/' + id,
        }
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    this.id = data.id
                    this.categoria = data.categoria
                    this.codigo = data.codigo
                    this.descripcion = data.descripcion
                    this.cantidad = data.cantidad
                    this.precioUnit = data.precioUnit
                    this.precioVPublico = data.precioVPublico
                })
                .catch(err => {
                    console.error(err);
                    this.error = true
                })
        },
        modificar() {
            let producto = {
                categoria: this.categoria,
                codigo: this.codigo,
                descripcion: this.descripcion,
                cantidad: this.cantidad,
                precioUnit: this.precioUnit,
                precioVPublico: this.precioVPublico,
            }
            var options = {
                body: JSON.stringify(producto),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url, options)
                .then(function() {
                    alert("Registro modificado")
                    window.location.href = "./index.html"; // navega a productos.html          
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Modificar")
                })
        }
    },
    created() {
        this.fetchData(this.url)
    },
}).mount('#app')