# Media Downloader

A powerful and easy-to-use media downloader for the OOMOL platform that lets you download videos and audio from popular websites like YouTube, Vimeo, TikTok, and many more.

## 🎯 What Can You Do?

With this media downloader, you can:

- **Download videos** from 1000+ supported websites
- **Extract audio** from video content
- **Choose video quality** (720p, 1080p, 4K when available)
- **Automatic format conversion** to MP4 for maximum compatibility
- **Batch downloads** using workflows
- **Custom save locations** - choose where your files go
- **Cookie support** for downloading private or age-restricted content

## 🧩 Available Blocks

### MediaDownloader Block

The main block that handles all your downloading needs.

**What it does:**
- Downloads videos and audio from any supported platform
- Automatically converts videos to MP4 format for universal playback
- Provides real-time download progress
- Handles authentication via cookie files when needed

**Inputs:**
- **Media URL** - The link to the video/audio you want to download
- **Save Location** - Where you want to save the file (optional - defaults to temporary storage)
- **Cookies** - Cookie file for accessing private content (optional)

**Output:**
- **File Path** - The location where your downloaded file was saved

## 🚀 How to Use

### Simple Download
1. Drag the **MediaDownloader** block into your workflow
2. Enter the URL of the media you want to download
3. Run the workflow
4. Your file will be downloaded automatically!

### Custom Save Location
1. Connect a file path to the "Save Location" input
2. Choose whether you want to specify a folder or exact filename
3. The downloader will save your file exactly where you want it

### Private Content Download
1. Export cookies from your browser for the website
2. Connect the cookie file to the "Cookies" input
3. The downloader can now access content that requires login

## 🌟 Use Cases

### Content Creators
- Download reference videos for editing projects
- Extract audio tracks for podcasts or music production
- Archive your own content from various platforms

### Educators
- Download educational videos for offline viewing
- Create local libraries of instructional content
- Prepare materials for presentations without internet dependency

### Personal Use
- Save favorite videos for offline viewing
- Download music and podcasts for travel
- Archive important content before it gets removed

### Business Applications
- Download training videos for employee onboarding
- Archive marketing content and competitor analysis
- Create offline presentations with multimedia content

## 🔧 Technical Features

- **Universal Compatibility**: Supports 1000+ websites including YouTube, Vimeo, TikTok, Twitter, Instagram, and more
- **Quality Options**: Automatically selects the best available quality up to 720p by default
- **Format Standardization**: Converts all downloads to MP4 for maximum device compatibility
- **Progress Tracking**: Real-time download progress with speed and percentage indicators
- **Error Handling**: Graceful handling of network issues and invalid URLs
- **Cookie Support**: Full authentication support via browser cookie import

## 📋 Supported Platforms

This downloader works with hundreds of websites, including:

- **Video Platforms**: YouTube, Vimeo, Dailymotion, Twitch
- **Social Media**: TikTok, Twitter, Instagram, Facebook
- **Educational**: Khan Academy, Coursera, edX
- **News & Media**: BBC, CNN, NBC, ABC
- **And many more...**

## 🛠️ Installation Requirements

The system automatically installs required dependencies:
- **yt-dlp**: The core downloading engine
- **FFmpeg**: For video processing and conversion
- **Python environment**: Managed automatically by OOMOL

## 📞 Support & Updates

- **Version**: 0.0.26
- **Repository**: [GitHub - Media Downloader](https://github.com/vince-hz/yt-dlp-downloader)
- **Latest Features**: Cookie content validation and improved error handling

## ⚖️ Legal Notice

Please respect copyright laws and website terms of service when downloading content. Only download content you have permission to download or that falls under fair use guidelines in your jurisdiction.

---

*Built for the OOMOL platform - Making media downloading simple and powerful for everyone.*