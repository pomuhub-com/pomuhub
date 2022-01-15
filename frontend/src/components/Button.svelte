<script>
    export let color;
    export let size;
</script>

<button class="size-{size} color-{color}"><slot></slot></button>

<style>
    button {
        border: 0;
        border-radius: 4px;
        text-align: center;
        outline: 0 none;
        vertical-align: top;
        cursor: pointer;
    }
    .size-thin {
        height: 26px;
        font-size: 12px;
        padding: 6px 10px;
    }
    .color-orange {
        color: #000;
        background-color: #f90;
    }
    .color-gray {
        color: #fff;
        background-color: #2f2f2f;
    }
    .color-gray:hover {
        background-color: #3f3f3f;
    }
</style>