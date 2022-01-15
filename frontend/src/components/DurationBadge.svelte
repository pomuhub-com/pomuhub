<script>
    import Fa from 'svelte-fa'
    import { onMount } from 'svelte';
    import { humanReadableElapsedHMS } from '../util/display.js';

    export let since;
    export let icons;

    let elapsed = Math.floor((new Date() - since) / 1000);
    $: temporalState = elapsed < 0 ? "until" : "since";
    $: icon = icons[temporalState];

    onMount(async () => {
        const interval = setInterval(() => {
            elapsed = Math.floor((new Date() - since) / 1000);
        }, 1000);
        return () => clearInterval(interval);
    });
</script>

<span class={temporalState}>
    {#if icon}<Fa icon={icon} />{/if}
    {humanReadableElapsedHMS(elapsed)}
</span>

<style>
    span {
        padding: 2px;
        border-radius: 3px;
        position: relative;
        float: right;
        z-index: 2;
        top: -30px;
        right: 5px;
        height: 15px;
        font-weight: bold;
        font-size: 10px;
    }
    .until {
        background-color: var(--theme-until-bg, #aaa);
        color: var(--theme-until-color, #333);
    }
    .since {
        background-color: var(--theme-since-bg, #f00);
        color: var(--theme-since-color, #fff);
    }
</style>