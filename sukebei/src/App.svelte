<script>
    import { onMount } from 'svelte';
    import DoujinGrid from './DoujinGrid.svelte';

    async function loadDoujinSet(path) {
        const res = await fetch(`/data/${path}.json`);
        if(res.status !== 200) {
            console.error(`Got unexpected ${res.status} when loading ${path}`);
            return [];
        }
        return (await res.json()).map(category => ({
            name: category.name,
            items: category.items.map(item => ({
                title: item.site_info?.title?.pretty ?? item.name,
                href: item.link,
                language: item.tags[0],
                cover: item.site_info?.cover?.src,
                tags: item.site_info?.tags ?? null,
            })),
        }));
    }

    let editions = {};
    let usePreviews = true;

    onMount(async () => {
        editions = {
            ange: [
                {
                    name: '2022',
                    doujinSet: await loadDoujinSet('ange/2022'),
                },
                {
                    name: '2021',
                    doujinSet: await loadDoujinSet('ange/2021'),
                }
            ],
        };
    });
</script>

<main>
    <button on:click={() => usePreviews = !usePreviews}>Toggle Preview Bluring</button>
    {#each Object.entries(editions) as [person, recommendations]}
    <h1>{person}</h1>
        {#each recommendations as {name, doujinSet}}
        <h2>{name}</h2>
            {#each doujinSet as category}
            <DoujinGrid
                title={category.name}
                doujins={category.items}
                blurred={usePreviews}
            />
            {/each}
        {/each}
    {/each}
</main>

<style>
    
    :global(body) {
        background-color: #000;
        margin: 0;
        padding: 0;
        font-size: 12px;
        font-family: Arial, Helvetica, sans-serif;
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
    main {
        max-width: 1323px;
        width: 96%;
        min-width: 991px;
        margin: 10px auto;
        padding: 20px 0;
        color: #ccc;
        max-width: 100%;
        min-width: 100%;
        margin-left: auto;
        margin-right: auto;
    }

    @media only screen and (min-width: 900px) {
        main {
            min-width: 75%;
            max-width: 75%;
        }
    }
</style>