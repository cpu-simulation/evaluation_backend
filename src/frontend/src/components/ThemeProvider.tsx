import { ReactNode, useState } from 'react'
const ThemeProvider = ({ children }: { children: ReactNode }) => {
  const [theme, _setTheme] = useState('light')
  return (
    <div id="theme-provider"
      className='bg-[--background] text-[--on-background]'
      data-theme={theme}>
      {children}
    </div>
  )
}

export default ThemeProvider
