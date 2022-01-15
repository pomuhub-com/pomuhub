<script>
    import DoujinCard from './DoujinCard.svelte';

    export let title;
    export let doujins;
    export let blurred;
</script>

<details open>
    <summary class="title">{title} - {doujins.length}</summary>
    <div class="grid">
        {#each doujins as doujin}
        <DoujinCard
            title={doujin.title}
            href={doujin.link}
            language={doujin.language}
            cover={doujin.cover}
            tags={doujin.tags}
            blurred={blurred}
        />
        {/each}
    </div>
</details>

<style>
    details {
        margin-bottom: 2em;
    }
    summary {
        margin-bottom: 1em;
        cursor: pointer;
    }

    .grid {
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
        max-width: 100%;
        min-width: 100%;
    }

    .title {
        color: #fff;
        font-weight: 700;
        text-transform: capitalize;
        font-size: 16px;
    }
</style>