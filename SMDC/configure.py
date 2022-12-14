def get_default_config(data_name):
    if data_name in ['Caltech101-20']:
        return dict(
            Autoencoder=dict(
                arch1=[1984, 1024, 1024, 1024, 128],
                arch2=[512, 1024, 1024, 1024, 128],
                attation_arch=[1024, 1024, 256, 1024],
                activations1='relu',
                activations2='relu',
                batchnorm=True,
            ),
            training=dict(
                seed=4,
                missing_rate=0,
                batch_size=256,
                epoch=500,
                lr=1.0e-4,
                # Balanced factors for L_cd, L_pre, and L_rec
                alpha=9,
                lambda1=0.1,
                lambda2=0.1,
            ),
        )
    elif data_name in ['Reuters_dim10']:
        """The default configs."""
        return dict(
            Autoencoder=dict(
                arch1=[59, 1024, 1024, 1024, 64],
                arch2=[40, 1024, 1024, 1024, 64],
                attation_arch=[1024, 1024, 256, 1024],
                activations1='relu',
                activations2='relu',
                batchnorm=True,
            ),
            training=dict(
                missing_rate=0,
                seed=3,
                epoch=1000,
                batch_size=256,
                lr=1.0e-4,
                alpha=9,
                lambda1=0.1,
                lambda2=0.1,
            ),
        )
    else:
        raise Exception('Undefined data_name')
