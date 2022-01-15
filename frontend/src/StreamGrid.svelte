<script>
    import Fa from 'svelte-fa'
    import { faAngleRight } from '@fortawesome/free-solid-svg-icons';
    import StreamCard from './StreamCard.svelte';

    export let streams;
    export let title;
</script>

<section>
    <h1 class="title">{title} <Fa icon={faAngleRight} /></h1>
    <div class="content">
        {#if streams.length > 0}
            {#each streams as stream}
                <StreamCard
                    thumbnail={stream.thumbnail}
                    title={stream.title}
                    startTime={stream.startTime}
                    viewers={stream.viewers}
                    channel={stream.channel}
                    streamHref={stream.streamHref}
                    channelHref={stream.channelHref}
                    status={stream.status}
                />
            {/each}
        {:else}
            <h2>No streams here</h2>
        {/if}
    </div>
</section>

<style>
    .content {
        display: grid;
        justify-content: center;
        align-content: center;
        grid-template-rows: auto;
        grid-template-columns: repeat(5, 1fr);
        grid-row-gap: 15px;
        grid-column-gap: 10px;
        margin-bottom: 20px;
    }
    h1, h2 {
        color: #fff;
        font-weight: 700;
        text-transform: capitalize;
    }
    h1 {
        font-size: 20px;
    }
    h2 {
        font-size: 16px;
    }
</style>