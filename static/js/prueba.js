const { createApp } = Vue
createApp({
    data() {
        return {
            productos: [],
            //url: 'https://pfbrodon.pythonanywhere.com/productos'
            url: 'http://127.0.0.1:5000/productos'
        }
    },
    methods: { // aqui se definen  las funciones del objeto VUE
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    this.productos = data
                })
                .catch(error => alert("Ups... se produjo un error: " + error))
        }
    },
    created() { //Se ejecuta cuando se carga el objeto VUE
        this.fetchData(this.url)
    }
}).mount('#app')