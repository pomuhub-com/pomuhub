<script>
    import { faCircle, faClock } from '@fortawesome/free-solid-svg-icons';
    import { humanReadableNumber } from './util/display.js';
    import DurationBadge from './components/DurationBadge.svelte';

    export let thumbnail;
    export let title;
    export let startTime;
    export let viewers;
    export let channel;
    export let channelHref;
    export let streamHref;
    export let status;

    const elapsedTime = Math.floor((new Date() - startTime) / 1000);
    const viewersDisplay = elapsedTime < 0 ? "waiting" : "viewers";
</script>

<div class="wrapper">
    <a href={streamHref} class="thumbnail">
        <img src={thumbnail}>
        {#if status !== "past"}
        <DurationBadge since={startTime} icons={{until: faClock, since: faCircle}} />
        {/if}
    </a>
    <div class="summary">
        <a href={streamHref} class="title">{title}</a>
        <div class="channel-info">
            <a href={channelHref} class="channel">{channel}</a>
        </div>
        <div class="video-info">
            {#if viewers !== null}
                <span class="viewers">
                    {`${humanReadableNumber(viewers)} ${viewersDisplay}`}
                </span>
            {/if}
        </div>
    </div>
</div>

<style>
    a {
        text-decoration: none;
        cursor: pointer;
    }
    a:hover {
        color: #f90;
    }
    .thumbnail {
        display: block;
    }
    .thumbnail > img {
        width: 100%;
        aspect-ratio: 1.7778;
    }
    .thumbnail > DurationBadge {
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
    .title {
        font-size: 15px;
        color: #c6c6c6;
    }
    .summary {
        font-size: 14px;
        color: #6a6a6a;
    }
    .channel {
        color: #6a6a6a;
    }
</style>