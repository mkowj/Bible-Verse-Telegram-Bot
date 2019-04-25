#Background
import logging
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

#Settled
def start(update, context):
    update.message.reply_text(
        'Feeling low? Please talk to me!\n'
        'Do you need /love, /inspiration or /help?')

#Settled
def love(update, context):
    love_verses = ["“He administers justice for the fatherless and the widow, and loves the stranger, giving him food and clothing.” - Deuteronomy 10:18", 
"“How precious is Your lovingkindness, O God! Therefore the children of men put their trust under the shadow of Your wings.” - Psalm 36:7", 
"“Because Your lovingkindness is better than life, my lips shall praise You.” - Psalm 63:3", 
"“As a father pities his children, so the LORD pities those who fear Him. For He knows our frame; He remembers that we are dust.” - Psalm 103:13-14", 
"“I will worship toward Your holy temple, and praise Your name for Your lovingkindness and Your truth; for You have magnified Your word above all Your name.” - Psalm 138:2", 
"“The LORD has appeared of old to me, saying, ‘Yes, I have loved you with an everlasting love; therefore with lovingkindness I have drawn you.’” - Jeremiah 31:3", 
"“The LORD your God in your midst, the Mighty One, will save; He will rejoice over you with gladness, He will quiet you with His love, He will rejoice over you with singing.” - Zephaniah 3:17", 
"“Now hope does not disappoint, because the love of God has been poured out in our hearts by the Holy Spirit [which] was given to us.” - Romans 5:5", 
"“But God demonstrates His own love toward us, in that while we were still sinners, Christ died for us.” - Romans 5:8", 
"“And we know that all things work together for good to those who love God, to those who are the called according to His purpose.” - Romans 8:28", 
"“Who shall separate us from the love of Christ? Shall tribulation, or distress, or persecution, or famine, or nakedness, or peril, or sword?” - Romans 8:35", 
"“Yet in all these things we are more than conquerors through Him who loved us. For I am persuaded that neither death nor life, nor angels nor principalities nor powers, nor things present nor things to come, nor height nor depth, nor any other created thing, shall be able to separate us from the love of God which is in Christ Jesus our Lord.” - Romans 8:37-39", 
"“But as it is written: ‘Eye has not seen, nor ear heard, nor have entered into the heart of man the things which God has prepared for those who love Him.’” - 1 Corinthians 2:9", 
"“But God, who is rich in mercy, because of His great love with which He loved us…” - Ephesians 2:4", 
"“To know the love of Christ which passes knowledge; that you may be filled with all the fullness of God.” - Ephesians 3:19", 
"“And walk in love, as Christ also has loved us and given Himself for us, an offering and a sacrifice to God for a sweet-smelling aroma.” - Ephesians 5:2", 
"“Therefore humble yourselves under the mighty hand of God, that He may exalt you in due time, casting all your care upon Him, for He cares for you.” - 1 Peter 5:6-7", 
"“If we confess our sins, He is faithful and just to forgive us our sins and to cleanse us from all unrighteousness.” - 1 John 1:9", 
"“Behold what manner of love the Father has bestowed on us, that we should be called children of God! Therefore the world does not know us, because it did not know Him.” - 1 John 3:1", 
"“He who does not love does not know God, for God is love. In this the love of God was manifested toward us, that God has sent His only begotten Son into the world, that we might live through Him. In this is love, not that we loved God, but that He loved us and sent His Son to be the propitiation for our sins.” - 1 John 4:8-10", 
"“And we have known and believed the love that God has for us. God is love, and he who abides in love abides in God, and God in him.” - 1 John 4:16"]
    love_machine = str(random.choice(love_verses))
    update.message.reply_text(love_machine)

def inspiration(update, context):
    inspiration_verses = ["“The LORD is my light and my salvation; whom shall I fear? The LORD is the strength of my life; of whom shall I be afraid?” - Psalm 27:1", 
"“But the salvation of the righteous is from the LORD; He is their strength in time of trouble.” - Psalm 37:39", 
"“In the day when I cried out, You answered me, and made me bold with strength in my soul.” - Psalm 138:3", 
"“But Jesus looked at them and said to them, ‘With men this is impossible, but with God all things are possible.’” - Matthew 19:26", 
"“Therefore we do not lose heart. Even though our outward man is perishing, yet the inward man is being renewed day by day.” - 2 Corinthians 4:16", 
"“I can do all things through Christ who strengthens me.” - Philippians 4:13", 
"“For God has not given us a spirit of fear, but of power and of love and of a sound mind.” - 2 Timothy 1:7", 
"“Out of the mouth of babes and nursing infants You have ordained strength, because of Your enemies, that You may silence the enemy and the avenger.” - Psalm 8:2", 
"“I will love You, O LORD, my strength. The LORD is my rock and my fortress and my deliverer; my God, my strength, in whom I will trust; my shield and the horn of my salvation, my stronghold.” - Psalm 18:1-2", 
"“It is God who arms me with strength, and makes my way perfect.” - Psalm 18:32", 
"“Let the words of my mouth and the meditation of my heart be acceptable in Your sight, O LORD, my strength and my Redeemer.” - Psalm 19:14", 
"“But You, O LORD, do not be far from Me; O My Strength, hasten to help Me!” - Psalm 22:19", 
"“The LORD is my strength and my shield; my heart trusted in Him, and I am helped; therefore my heart greatly rejoices, and with my song I will praise Him. The LORD is their strength, and He is the saving refuge of His anointed.” - Psalm 28:7-8", 
"“The LORD will give strength to His people; the LORD will bless His people with peace.” - Psalm 29:11", 
"“God is our refuge and strength, a very present help in trouble.” - Psalm 46:1", "“Save me, O God, by Your name, and vindicate me by Your strength.” - Psalm 54:1", 
"“Who established the mountains by His strength, being clothed with power.” - Psalm 65:6", 
"“I will go in the strength of the Lord GOD; I will make mention of Your righteousness, of Yours only.” - Psalm 71:16", 
"“My flesh and my heart fail; but God is the strength of my heart and my portion forever.” - Psalm 73:26", 
"“The LORD is my strength and song, and He has become my salvation.” - Psalm 118:14", 
"“The LORD is my strength and song, and He has become my salvation; He is my God, and I will praise Him; my father’s God, and I will exalt Him.” - Exodus 15:2", 
"“The God of my strength, in whom I will trust; my shield and the horn of my salvation, my stronghold and my refuge; my Savior, You save me from violence.” - 2 Samuel 22:3", 
"“Seek the LORD and His strength; seek His face evermore!” - 1 Chronicles 16:11", 
"“Both riches and honor come from You, and You reign over all. In Your hand is power and might; in Your hand it is to make great and to give strength to all.” - 1 Chronicles 29:12", 
"“Then he said to them, ‘Go your way, eat the fat, drink the sweet, and send portions to those for whom nothing is prepared; for this day is holy to our Lord. Do not sorrow, for the joy of the LORD is your strength.” - Nehemiah 8:10", 
"“Behold, God is my salvation, I will trust and not be afraid; ‘For YAH, the LORD, is my strength and song; He also has become my salvation.” - Isaiah 12:2", 
"“For You have been a strength to the poor, a strength to the needy in his distress, a refuge from the storm, a shade from the heat; for the blast of the terrible ones is as a storm against the wall.” - Isaiah 25:4", 
"“He gives power to the weak, and to those who have no might He increases strength. But those who wait on the LORD shall renew their strength; they shall mount up with wings like eagles, they shall run and not be weary, they shall walk and not faint.” - Isaiah 40:29, 31", 
"“Fear not, for I am with you; be not dismayed, for I am your God. I will strengthen you, yes, I will help you, I will uphold you with My righteous right hand.” - Isaiah 41:10", 
"“Ah, Lord GOD! Behold, You have made the heavens and the earth by Your great power and outstretched arm. There is nothing too hard for You.” - Jeremiah 32:17", 
"“The LORD God is my strength; He will make my feet like deer’s feet, and He will make me walk on my high hills.” - Habakkuk 3:19", 
"“‘Not by might nor by power, but by My Spirit,’ says the LORD of hosts.” - Zechariah 4:6", 
"“But you shall receive power when the Holy Spirit has come upon you; and you shall be witnesses to Me in Jerusalem, and in all Judea and Samaria, and to the end of the earth.” - Acts 1:8", 
"“That He would grant you, according to the riches of His glory, to be strengthened with might through His Spirit in the inner man.” - Ephesians 3:16", 
"“Now to Him who is able to do exceedingly abundantly above all that we ask or think, according to the power that works in us, to Him be the glory in the church by Christ Jesus to all generations, forever and ever. Amen.” - Ephesians 3:20-21", 
"“Finally, my brethren, be strong in the Lord and in the power of His might.” - Ephesians 6:10", 
"“But the Lord is faithful, who will establish you and guard you from the evil one.” - 2 Thessalonians 3:3"]
    inspiration_machine = str(random.choice(inspiration_verses))
    update.message.reply_text(inspiration_machine)

#Settled
def help(update, context):
    update.message.reply_text('Haha! Fool!')

#Settled
def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

#Settled(?)
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("864560514:AAEQ8TO2VBu2_KpFVd_myp-d1TFf75CbZMI", use_context=True)

    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("love", love))
    dp.add_handler(CommandHandler("inspiration", inspiration))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()