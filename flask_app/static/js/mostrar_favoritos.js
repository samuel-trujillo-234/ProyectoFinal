// Coding Dojo - Python Bootcamp Jan 2025
// Final project
// Wavely - Scripts Java

//
// Funciones utilizadas para manejar favoritos y filtors de exibición

document.addEventListener('DOMContentLoaded', function () {

    // Manejar los filtros activos
    const activeFilters = document.querySelector('.active-filters');
    const selects = document.querySelectorAll('.organization-section select');

    selects.forEach(select => {
        select.addEventListener('change', function () {
            if (this.value !== this.options[0].value) {
                // Crear nueva etiqueta de filtro
                const badge = document.createElement('span');
                badge.className = 'badge bg-primary d-flex align-items-center';
                badge.innerHTML = `
                    ${this.options[this.selectedIndex].text}
                    <button type="button" class="btn-close btn-close-white ms-2" aria-label="Close"></button>
                `;

                // Agregar funcionalidad para eliminar el filtro
                const closeBtn = badge.querySelector('.btn-close');
                closeBtn.addEventListener('click', function () {
                    badge.remove();
                    select.selectedIndex = 0;
                    // Aquí iría la lógica para reordenar/filtrar las noticias
                    reorderNews();
                });

                // Agregar el nuevo filtro
                activeFilters.appendChild(badge);

                // Aquí iría la lógica para reordenar/filtrar las noticias
                reorderNews();
            }
        });
    });

    // Función para reordenar noticias (ejemplo básico)
    function reorderNews() {
        const newsContainer = document.querySelector('.news-container');
        const news = Array.from(newsContainer.querySelectorAll('.card'));
        const orderSelect = document.querySelector('select[aria-label="Ordenar por"]');

        // Ejemplo de ordenamiento por fecha
        if (orderSelect.value === 'date_desc') {
            news.sort((a, b) => {
                const dateA = a.querySelector('.news-meta').textContent;
                const dateB = b.querySelector('.news-meta').textContent;
                return dateB.localeCompare(dateA);
            });
        } else if (orderSelect.value === 'date_asc') {
            news.sort((a, b) => {
                const dateA = a.querySelector('.news-meta').textContent;
                const dateB = b.querySelector('.news-meta').textContent;
                return dateA.localeCompare(dateB);
            });
        } else if (orderSelect.value === 'likes') {
            news.sort((a, b) => {
                const likesA = parseInt(a.querySelector('.like .counter').textContent);
                const likesB = parseInt(b.querySelector('.like .counter').textContent);
                return likesB - likesA;
            });
        }

        // Limpiar y reordenar las noticias
        news.forEach(card => newsContainer.appendChild(card));

        // Agregar animación de transición
        news.forEach((card, index) => {
            card.style.opacity = '0';
            setTimeout(() => {
                card.style.transition = 'opacity 0.3s ease';
                card.style.opacity = '1';
            }, index * 100);
        });
    }
});