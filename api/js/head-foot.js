//Agregamos header con javascript:

let hea = `

<a href="../index.html"><img src="../img/logo_buloneria.png" alt="" class="logo"></a>
        <button class="abrir-menu" id="abrir"><i class="bi bi-list"></i></button>
        
        <div class="nav-header" id="nav-header">
            <button class="cerrar-menu" id="cerrar"><i class="bi bi-x"></i></button>
            <ul class="nav-list-c">
                <li><a href="../html/productos.html">Productos</a></li>
                <li><a href="../html/quienes.html">Quienes Somos</a></li>
                <li><a href="../html/registro.html">Registro</a></li>
                <li><a href="../html/contacto.html">Contacto</a></li>
            </ul>
        
        </div>`;

document.querySelector("header").innerHTML = hea;

//agregamos footer con javascript:

let foot = `
<div class="footer-grid">
   
        <section class="footer-1">
          <h4>Nuestras Redes</h4>
          <br>
          <a href="http://facebook.com"><img src="../img/logo-face.png" alt="facebook"></a>
          <a href="http://instagram.com"><img src="../img/logo-inst.png" alt="instagram"></a>
          <a href="http://twitter.com"><img src="../img/logo-tw.png" alt="twitter"></a>
          <a href="http://linkedin.com"><img src="../img/logo-linked.png" alt="linkedin"></a>
        </section>

       <section class="footer-2">
          <h4>Donde contactarnos</h4>
          <p>Direccion: Calle Falsa 123, CABA</p>
          <p>Telefono: 1112345678</p>
          <p>Email: buloneria@contacto.com.ar</p>
          
        </section>

       <section class="footer-3">
         <h4>Donde estamos</h4>
         <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d210161.67554404985!2d-58.697476705468716!3d-34.6098208!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccac2cd859503%3A0x75cdafaaef2b946!2sCongreso%20de%20la%20Naci%C3%B3n%20Argentina!5e0!3m2!1ses-419!2sar!4v1697994222541!5m2!1ses-419!2sar"  style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
       </section>

      
   </div>
   <p class="copy">Copyright 2023© -
   Página Web Desarrollada en Curso Codo a Codo</p>
   `;

document.querySelector("footer").innerHTML = foot;