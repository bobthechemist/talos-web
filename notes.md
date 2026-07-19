# Tips for making the website content

## AR page

No gifs allowed. Use ffmpeg to convert to mp4.

`ffmpeg -i my_animation.gif -movflags faststart -pix_fmt yuv420p my_animation.mp4`
`ffmpeg -i your_animation.gif -vf "crop=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -pix_fmt yuv420p -movflags faststart output_animation.mp4`

Screen capture for CMD display: 0.5 bitrate, disable audio, 2 pass, set command prompt font to 36

**Will need to try including the markers in the screen capture. Have a powerpoint slide, white background with markers and position the cmd prompt in that.**

Added a targets directory for the images used on the poster.


workflow
- Create video 
- Capture frame that will be used on poster
- add stills to `targets` and label them with a number 
- add videos to `videos` and make sure name aligns with still
- update index.html to have the right files loaded
- recreate targets.mind https://hiukim.github.io/mind-ar-js-doc/tools/compile/
- push changes