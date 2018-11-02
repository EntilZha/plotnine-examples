(
    ggplot(df_test)
    + aes(
        x='Guesser',
        fill='wiki',
        ymin='mean_accuracy - std_dev', ymax='mean_accuracy + std_dev'
    )
    + geom_bar(aes(y='best_accuracy'), stat='identity', position='dodge')
    + geom_errorbar(size=.5, width=.5, position=position_dodge(.9))
    + facet_wrap(['Metric'], labeller='label_both')
    + theme(axis_text_x=element_text(angle=45, hjust=1))
    + ylab('Accuracy on Test Fold')
)
