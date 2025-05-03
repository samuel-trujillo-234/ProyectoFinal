// Coding Dojo - Python Bootcamp Jan 2025
// Final project
// Wavely - Scripts Java



//
// Funciones utilizadas para administrar usuarios


document.addEventListener('DOMContentLoaded', function () {
    // Inicializar DataTables
    $('#users-table').DataTable({
        language: {
        url: '//cdn.datatables.net/plug-ins/1.11.5/i18n/es-ES.json'
        },
        responsive: true
    });

// Configurar modal de eliminación
const deleteModal = document.getElementById('deleteModal');
deleteModal.addEventListener('show.bs.modal', function (event) {
    const button = event.relatedTarget;
    const userId = button.getAttribute('data-user-id');
    document.getElementById('deleteUserId').value = userId;
});

// Editar categoría de usuario
const editButtons = document.querySelectorAll('.edit-categoria');
editButtons.forEach(button => {
    button.addEventListener('click', function () {
    const userId = this.getAttribute('data-user-id');
    const row = this.closest('tr');
    const categoriaText = row.querySelector('.categoria-text');
    const categoriaSelect = row.querySelector('.categoria-select');
    
    if (categoriaText.classList.contains('d-none')) {
    
        // Guardar cambios - Enviamos el formulario
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = '/update_user_categoria';

       // Añadir los campos del formulario
        const userIdInput = document.createElement('input');
        userIdInput.type = 'hidden';
        userIdInput.name = 'user_id';
        userIdInput.value = userId;

        const categoriaInput = document.createElement('input');
        categoriaInput.type = 'hidden';
        categoriaInput.name = 'categoria';
        categoriaInput.value = categoriaSelect.value;

       // Añadir inputs al formulario
        form.appendChild(userIdInput);
        form.appendChild(categoriaInput);

       // Añadir formulario al documento y enviarlo
        document.body.appendChild(form);
        form.submit();
    
    } else {
      // Mostrar selector
        categoriaText.classList.add('d-none');
        categoriaSelect.classList.remove('d-none');
        this.innerHTML = '<i class="fas fa-save"></i> Guardar';
    }
    });
});
});