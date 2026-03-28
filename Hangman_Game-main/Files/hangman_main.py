from hangman_assets import cleanScreen, timeWait, writeScreen, playersNames, wordTips, infoWord, options

cleanScreen()

writeScreen(f"{'#' * 25}\n{'#' * 7} BEM VINDO {'#' * 7}\n{'#' * 5} JOGO DA FORCA {'#' * 5}\n{'#' * 25}")
timeWait(2)

playersNames()
wordTips()
infoWord()
options()
