// Coding Dojo - Python Bootcamp Jan 2025
// Proyecto final
// Wavely - Scripts Java

//
// Funciones para reportar noticias

// Función para manejar los reports
function handleReport(button) {
    const noticiaId = button.getAttribute('data-id');
    
    if (button.classList.contains('active')) {
        // Cancelar report
        fetch(`/cancelar_report/${noticiaId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(function(response) {
            return response.json(); // Parse the JSON response
        })
        .then(function(data) {
            if (data.success) {
                button.classList.remove('active');
                const icon = button.querySelector('i');
                if (icon) {
                    icon.style.color = ''; // Restablecer color
                }
                const counter = button.querySelector('.counter');
                if (counter) {
                    // Use the count from the server instead of manually decrementing
                    counter.textContent = data.count || 0;
                }
                // Mostrar mensaje de éxito usando toastr si existe
                if (window.toastr) {
                    toastr.success('Reporte cancelado correctamente');
                }
            }
        })
        .catch(function(error) {
            console.error('Error al cancelar reporte:', error);
        });
    } else {
        // Crear report
        fetch(`/reportar_noticia/${noticiaId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(function(response) {
            return response.json(); // Parse the JSON response
        })
        .then(function(data) {
            if (data.success) {
                button.classList.add('active');
                const icon = button.querySelector('i');
                if (icon) {
                    icon.style.color = '#ff4136'; // Color rojo para reportes
                }
                const counter = button.querySelector('.counter');
                if (counter) {
                    // Use the count from the server instead of manually incrementing
                    counter.textContent = data.count || 0;
                }
                // Mostrar mensaje de éxito usando toastr si existe
                if (window.toastr) {
                    toastr.success('Noticia reportada correctamente');
                }
            }
        })
        .catch(function(error) {
            console.error('Error al reportar noticia:', error);
        });
    }
}

// Función para inicializar los botones de report
function updateCounter(button, action) {
    const counter = button.querySelector('.counter');
    let count = parseInt(counter.textContent);
    counter.textContent = count + 1;
    button.classList.add('active');
    
    // Cambiar el color del ícono si es el botón de reports
    if (action === 'favorite') {
        const icon = button.querySelector('i');
        icon.style.color = '#ffd700';
    }
}