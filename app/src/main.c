/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/init.h>
#include <zephyr/settings/settings.h>

#include <zephyr/logging/log.h>
LOG_MODULE_REGISTER(zmk, CONFIG_ZMK_LOG_LEVEL);

#include <zmk/matrix.h>
#include <zmk/kscan.h>
#include <zmk/display.h>
#include <drivers/ext_power.h>

#if DT_NODE_EXISTS(DT_NODELABEL(oled_pwr))
static int oled_pwr_init(const struct device *)
{
    const struct gpio_dt_spec oled_pwr = GPIO_DT_SPEC_GET(DT_NODELABEL(oled_pwr), gpios);
    gpio_pin_configure_dt(&oled_pwr, GPIO_OUTPUT_ACTIVE);

    return 0;
}

SYS_INIT(oled_pwr_init, PRE_KERNEL_1, 0);
#endif

void main(void) {
    LOG_INF("Welcome to ZMK!\n");

    if (zmk_kscan_init(DEVICE_DT_GET(ZMK_MATRIX_NODE_ID)) != 0) {
        return;
    }

#ifdef CONFIG_ZMK_DISPLAY
    zmk_display_init();
#endif /* CONFIG_ZMK_DISPLAY */
}
