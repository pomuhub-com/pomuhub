<script>
    export let title;
    export let href;
    export let language;
    export let cover;
    export let tags;
    export let blurred;

    const coverId = cover?.match(/https:\/\/t.nhentai.net\/galleries\/(\d+)\/cover.jpg/);
    cover = coverId && `/images/nhentai/${coverId[1]}.jpg`;
</script>

<a href={href} rel="noreferrer noopener" class="card">
    {#if cover}
    <img class="{blurred && "blurred"}" loading="lazy" src={cover} alt={title} />
    {/if}
    <div class="content">
        <div class="lang">{language}</div>
        <div class="title">{title}</div>
    </div>
</a>


<style>
    .card {
        display: grid;
        height: 300px;
        aspect-ratio: 0.618;
        overflow: hidden;
        text-decoration: none;
        color: #ccc;
        background: #333;
    }
    .card > .content {
        z-index: 2;
    }
    .card > * {
        grid-column: 1;
        grid-row: 1;
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: row;
        float: left;
    }
    .card .lang {
        position: absolute;
        margin: 3px;
    }
    .card .title {
        align-self: flex-end;
        background-color: rgba(51, 51, 51, 0.8);
        padding: 5px;
        max-height: 3.5em;
        overflow-y: hidden;
        width: 100%;
    }
    .blurred {
        filter: blur(10px);
    }
</style>