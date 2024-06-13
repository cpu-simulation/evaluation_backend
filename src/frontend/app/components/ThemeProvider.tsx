'use client'
import { ReactNode, useEffect, useState } from 'react'
const ThemeProvider = ({ children }: { children: ReactNode }) => {

  // const themeConfig = "auto"
  const [theme, setTheme] = useState('light')
  // useEffect(() => {
  //   if (themeConfig === 'auto') {
  //     setTheme(getOsTheme())
  //   } else {
  //     setTheme(themeConfig)
  //   }
  // }, [themeConfig])

  // const getOsTheme = () => {
  //   const media = '(prefers-color-scheme: dark)'
  //   if (window.matchMedia(media).matches) {
  //     return 'dark'
  //   } else {
  //     return 'light'
  //   }
  // }

  return (
    <div id="theme-provider"
      className='bg-[--background] text-[--on-background]'
      data-theme={theme}>
      {children}
    </div>
  )
}

export default ThemeProvider
