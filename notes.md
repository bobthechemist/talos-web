# Tips for making the website content

## AR page

No gifs allowed. Use ffmpeg to convert to mp4.

`ffmpeg -i my_animation.gif -movflags faststart -pix_fmt yuv420p my_animation.mp4`
`ffmpeg -i your_animation.gif -vf "crop=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -pix_fmt yuv420p -movflags faststart output_animation.mp4`

Screen capture for CMD display: 0.5 bitrate, disable audio, 2 pass, set command prompt font to 36