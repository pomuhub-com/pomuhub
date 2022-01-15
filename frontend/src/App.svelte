<script>
    import Fa from 'svelte-fa'
    import { faGithub } from '@fortawesome/free-brands-svg-icons';
    import { faSearch, faCalendar } from '@fortawesome/free-solid-svg-icons';
    import { onMount } from 'svelte';
    import StreamGrid from './StreamGrid.svelte';
    import Button from './components/Button.svelte';

    let streams = [];
    onMount(async () => {
        const res = await fetch('/api/data');
        const data = await res.json();
        streams = data
            .filter(stream => !(["missing"].includes(stream.status.toLowerCase())))
            .map(stream => ({
                thumbnail: `https://i.ytimg.com/vi/${stream.id}/mqdefault.jpg`,
                title: stream.title,
                startTime: new Date(stream.start_actual ?? stream.start_scheduled),
                viewers: stream.live_viewers ?? 0,
                channel: stream.channel.english_name ?? stream.channel.name,
                channelHref: `https://www.youtube.com/channel/${stream.channel.id}`,
                streamHref: `https://www.youtube.com/watch/${stream.id}`,
                status: stream.status,
            }));
    });

    let now = Date.now();

    let liveStreams = streams.filter(a => now > a.startTime && a.status !== "past");
    let scheduledStreams = streams.filter(a => now <= a.startTime && (a.startTime - now) < 7*24*60*60*1000);
    let recentStreams = streams.filter(a => a.status === "past").sort((a, b) => a.startTime - b.startTime).slice(0, 20);

    let sortedScheduledStreams = scheduledStreams.sort((a, b) => a.startTime - b.startTime);

    $: {
        now = Date.now();

        liveStreams = streams.filter(a => now > a.startTime && a.status !== "past");
        scheduledStreams = streams.filter(a => now <= a.startTime && (a.startTime - now) < 7*24*60*60*1000);
        recentStreams = streams.filter(a => a.status === "past").sort((a, b) => a.startTime - b.startTime).slice(0, 20);
        sortedScheduledStreams = scheduledStreams.sort((a, b) => a.startTime - b.startTime);
        if(sortedScheduledStreams.length > 0) {
            const closestStream = sortedScheduledStreams[0];
            setTimeout(
                () => {
                    console.log(closestStream);
                    // TODO: id
                    liveStreams = [...liveStreams, closestStream];
                    scheduledStreams = scheduledStreams.filter(stream => stream.startTime != closestStream.startTime);
                },
                closestStream.startTime - Date.now(),
            );
        }
    }
    
    setTimeout(() => window.location.reload(), 5 * 60 * 1000);
</script>

<div class="header-wrapper">
    <header>
        <div>
            <img src="images/logo.png" alt="pomuhub" height="29" width="150">
        </div>
        <div class="search-wrapper">
            <input type="search" placeholder="Search videos">
            <button type="submit">
                <Fa icon={faSearch} />
            </button>
        </div>
        <div>
            <a href="https://github.com" rel="noreferrer noopener">
                <Button size="thin" color="gray"><Fa icon={faGithub} /> Source</Button>
            </a>
            <a href="https://holodex.net/" rel="noreferrer noopener">
                <Button size="thin" color="orange"><Fa icon={faCalendar} /> Holodex</Button>
            </a>
        </div>
        <div class="auth-wrapper">
            <a href="javascript:void(alert('This is a meme site :P use holodex'))" style="grid-column-start: 2">Login</a>
            <a href="javascript:void(alert('This is a meme site :P use holodex'))" style="grid-column-start: 3">Sign Up</a>
        </div>
    </header>
    <nav>
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">Topics</a></li>
            <li><a href="#">Channels</a></li>
            <li><a href="#">Organizations</a></li>
            <li><a href="#">Archive</a></li>
        </ul>
    </nav>
</div>

<main>
    <StreamGrid title="Live Streams" streams={liveStreams} />
    <StreamGrid title="Scheduled Streams" streams={scheduledStreams} />
    <StreamGrid title="Recent Streams" streams={recentStreams} />
</main>

<style>
    :global(body) {
        background-color: #000;
        margin: 0;
        padding: 0;
        font-size: 12px;
        font-family: Arial, Helvetica, sans-serif;
    }
    nav {
        width: 100%;
        height: 40px;
        border-top: 1px solid #242424;
        display: grid;
        align-items: center;
        justify-items: center;
    }
    nav > ul {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        justify-items: center;
        align-items: center;
        max-width: 1323px;
        min-width: 991px;
        width: 96%;
        list-style-type: none;
        margin: auto;
        color: #fff;
        text-transform: uppercase;
        font-size: 12px;
        font-weight: bold;
        height: 100%;
    }
    nav > ul > li {
        height: 100%;
        width: 100%;
        display: grid;
        align-items: center;
        text-align: center;
    }
    nav > ul > li > a {
        display: block;
    }
    nav > ul > li:hover {
        text-transform: uppercase;
        background-color: #191919;
        border-left: 1px solid #252525;
        border-right: 1px solid #252525;
    }
    .search-wrapper {
        height: 26px;
        width: 100%;
        display: grid;
        grid-template-columns: 7fr minmax(48px,1fr);
    }
    .search-wrapper > * {
        height: 100%;
        font-size: 14px;
        padding: 2px 5px;
        vertical-align: top;
        border: none;
        display: inline-block;
        position: relative;
        top: -5px;
    }
    .auth-wrapper {
        display: grid;
        grid-template-columns: .5fr 2fr 1fr;
        grid-gap: 3px;
        align-items: center;
        grid-column-start: 4;
        width: 100%;
        justify-items: end;
        font-size: 12px;
        float: right;
    }
    a:hover {
        text-decoration: none;
        color: #fff;
    }
    input {
        border-radius: 3px 0 0 3px;
        color: #cacaca;
        background-color: #363636;
        outline: 0;
    }
    input[type="search"]:placeholder-shown {
        font-style: italic
    }
    button[type="submit"] {
        border-radius: 0 3px 3px 0;
        color: #000;
        background-color: #f90;
    }
    a {
        color: #ccc;
    }
    .header-wrapper {
        background-color: #1b1b1b;
        width: 100%;
    }
    header {
        padding: 10px;
        margin: auto;
        max-width: 1323px;
        display: grid;
        grid-gap: 10px;
        grid-template-columns: 200px 1fr 250px 220px;
        align-items: center;
        justify-items: center;
    }
    img {
        min-height: 40px;
    }
    main {
        max-width: 1323px;
        width: 96%;
        min-width: 991px;
        margin: 10px auto;
        padding: 20px 0;
    }
</style>