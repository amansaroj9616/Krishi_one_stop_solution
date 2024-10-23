<script>
    document.addEventListener('DOMContentLoaded', function() {
        const inputs = document.querySelectorAll('input[type="number"]');

        inputs.forEach(input => {
            input.addEventListener('input', function() {
                const min = parseFloat(input.getAttribute('min'));
                const max = parseFloat(input.getAttribute('max'));
                const value = parseFloat(input.value);

                // Check if value exceeds limits and adjust accordingly
                if (value < min) {
                    input.value = min;
                } else if (value > max) {
                    input.value = max;
                }
            });
        });
    });
</script>
